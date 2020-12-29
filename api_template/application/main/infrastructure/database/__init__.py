from pydantic.dataclasses import dataclass

from application.main.infrastructure.database.mongodb.operations import Mongodb


DataBaseToUse ={'mongodb' : Mongodb() }