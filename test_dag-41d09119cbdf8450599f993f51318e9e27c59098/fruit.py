import ray
from ray import serve
from ray.serve.drivers import DAGDriver
from ray.serve.deployment_graph import InputNode

# These imports are used only for type hints:
from typing import Dict, List
from starlette.requests import Request
from ray.serve.deployment_graph import ClassNode
from ray.serve.handle import RayServeDeploymentHandle


@serve.deployment(num_replicas=2)
class FruitMarket:
    def __init__(
        self,
        mango_stand: RayServeDeploymentHandle,
        orange_stand: RayServeDeploymentHandle,
        pear_stand: RayServeDeploymentHandle,
    ):
        self.directory = {
            "MANGO": mango_stand,
            "ORANGE": orange_stand,
            "PEAR": pear_stand,
        }

    async def check_price(self, fruit: str, amount: float) -> float:
        if fruit not in self.directory:
            return -1
        else:
            fruit_stand = self.directory[fruit]
            return await (await fruit_stand.check_price.remote(amount))


@serve.deployment(user_config={"price": 3})
class MangoStand:

    DEFAULT_PRICE = 1

    def __init__(self):
        # This default price is overwritten by the one specified in the
        # user_config through the reconfigure() method.
        self.price = self.DEFAULT_PRICE

    def reconfigure(self, config: Dict):
        self.price = config.get("price", self.DEFAULT_PRICE)

    def check_price(self, amount: float) -> float:
        return self.price * amount


@serve.deployment(user_config={"price": 2})
class OrangeStand:

    DEFAULT_PRICE = 0.5

    def __init__(self):
        # This default price is overwritten by the one specified in the
        # user_config through the reconfigure() method.
        self.price = self.DEFAULT_PRICE

    def reconfigure(self, config: Dict):
        self.price = config.get("price", self.DEFAULT_PRICE)

    def check_price(self, amount: float) -> float:
        return self.price * amount


@serve.deployment(user_config={"price": 4})
class PearStand:

    DEFAULT_PRICE = 0.75

    def __init__(self):
        # This default price is overwritten by the one specified in the
        # user_config through the reconfigure() method.
        self.price = self.DEFAULT_PRICE

    def reconfigure(self, config: Dict):
        self.price = config.get("price", self.DEFAULT_PRICE)

    def check_price(self, amount: float) -> float:
        return self.price * amount


async def json_resolver(request: Request) -> List:
    return await request.json()


with InputNode() as query:
    fruit, amount = query[0], query[1]

    mango_stand = MangoStand.bind()
    orange_stand = OrangeStand.bind()
    pear_stand = PearStand.bind()

    fruit_market = FruitMarket.bind(mango_stand, orange_stand, pear_stand)

    net_price = fruit_market.check_price.bind(fruit, amount)

deployment_graph = DAGDriver.bind(net_price, http_adapter=json_resolver)
