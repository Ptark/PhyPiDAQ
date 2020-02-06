from abc import ABC
from enum import Enum, unique
from typing import Type

from PyQt5.QtWidgets import QWidget

from ...SystemInfo import SystemInfo
from ...model.item.AccelerationSensorItem import AccelerationSensorItem
from ...model.item.DiagramItem import DiagramItem, TimeDiagramItem, DualDiagramItem, BarDiagramItem
from ...model.item.DistanceSensorItem import DistanceSensorItem
from ...model.item.ForceSensorItem import ForceSensorItem
from ...model.item.ItemModel import ItemModel
from ...model.item.OperatorItem import AdditionOperatorItem, SubtractionOperatorItem, \
    MultiplicationOperatorItem, DivisionOperatorItem, AbsoluteOperatorItem, OperatorItem
from ...model.item.SensorItem import SensorItem
from ...model.item.TemperatureSensorItem import TemperatureSensorItem
from ..DiagramField.DiagramView import DiagramView, TimeDiagram, DualDiagram, BarDiagram
from .DiagramItemView import DiagramItemView
from .OperatorItemView import OperatorItemView
from .SensorItemView import SensorItemView
from .WorkspaceItemView import WorkspaceItemView


class ItemEnumMeta(type(ABC), type(Enum)):
    pass


@unique
class ItemEnum(ABC, Enum, metaclass=ItemEnumMeta):
    def __init__(self, view: Type[WorkspaceItemView], model: Type[ItemModel], file: str):
        self.__view: Type[WorkspaceItemView] = view
        self.__model: Type[ItemModel] = model
        self.__path: str = SystemInfo.RESOURCES + 'images/items/' + file + '.svg'

    @property
    def model(self) -> Type[ItemModel]:
        return self.__model

    @property
    def path(self) -> str:
        return self.__path

    def create_workspace_item(self, parent: QWidget) -> WorkspaceItemView:
        return self.__view(parent, self)


@unique
class SensorEnum(ItemEnum):
    TEMPERATURE_SENSOR = (TemperatureSensorItem, 'temperature')
    FORCE_SENSOR = (ForceSensorItem, 'force')
    DISTANCE_SENSOR = (DistanceSensorItem, 'distance')
    ACCELERATION_SENSOR = (AccelerationSensorItem, 'acceleration')

    def __init__(self, model: Type[SensorItem], file: str):
        super().__init__(SensorItemView, model, 'sensor/' + file)


@unique
class OperatorEnum(ItemEnum):
    ADDITION_OPERATOR = (AdditionOperatorItem, 'addition')
    SUBTRACTION_OPERATOR = (SubtractionOperatorItem, 'subtraction')
    MULTIPLICATION_OPERATOR = (MultiplicationOperatorItem, 'multiplication')
    DIVISION_OPERATOR = (DivisionOperatorItem, 'division')
    ABSOLUTE_OPERATOR = (AbsoluteOperatorItem, 'absolute')

    def __init__(self, model: Type[OperatorItem], file: str):
        super().__init__(OperatorItemView, model, 'operator/' + file)


@unique
class DiagramEnum(ItemEnum):
    TIME_DIAGRAM = (TimeDiagramItem, 'time', TimeDiagram)
    DUAL_DIAGRAM = (DualDiagramItem, 'dual', DualDiagram)
    BAR_DIAGRAM = (BarDiagramItem, 'bar', BarDiagram)

    def __init__(self, model: Type[DiagramItem], file: str, diagram: Type[DiagramView]):
        self.__diagram: Type[DiagramView] = diagram
        super().__init__(DiagramItemView, model, 'diagram/' + file)

    @property
    def diagram(self) -> Type[DiagramView]:
        return self.__diagram
