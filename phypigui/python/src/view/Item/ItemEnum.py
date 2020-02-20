from abc import ABC
from enum import Enum, unique
from typing import Type

from PyQt5.QtWidgets import QWidget

from ...SystemInfo import SystemInfo
from ...model.item.sensors.AccelerationSensorItem import AccelerationSensorItem
from ...model.item.sensors.ConstantItems import ConstantItem, NatureConstantItem
from ...model.item.sensors.CurrentSensorItem import CurrentSensorItem
from ...model.item.diagrams.DiagramItem import DiagramItem
from ...model.item.diagrams.TimeDiagramItem import TimeDiagramItem
from ...model.item.diagrams.DualDiagramItem import DualDiagramItem
from ...model.item.diagrams.ThreeDimDiagramItem import ThreeDimDiagramItem
from ...model.item.diagrams.BarDiagramItem import BarDiagramItem
from ...model.item.sensors.DistanceSensorItem import DistanceSensorItem
from ...model.item.sensors.ForceSensorItem import ForceSensorItem
from ...model.item.ItemModel import ItemModel
from ...model.item.operators.OperatorItem import OperatorItem
from ...model.item.operators.AdditionOperatorItem import AdditionOperatorItem
from ...model.item.operators.SubtractionOperatorItem import SubtractionOperatorItem
from ...model.item.operators.MultiplicationOperatorItem import MultiplicationOperatorItem
from ...model.item.operators.DivisionOperatorItem import DivisionOperatorItem
from ...model.item.operators.AbsoluteOperatorItem import AbsoluteOperatorItem
from ...model.item.operators.NegativeOperatorItem import NegativeOperatorItem
from ...model.item.operators.PowerOperatorItem import PowerOperatorItem, MagnitudeOperatorItem
from ...model.item.operators.RootOperatorItem import RootOperatorItem
from ...model.item.operators.CloneItem import CloneItem
from ...model.item.sensors.ProxySensorItem import ProxySensorItem
from ...model.item.sensors.RGBSensorItem import RGBSensorItem
from ...model.item.sensors.SensorItem import SensorItem
from ...model.item.sensors.TemperatureSensorItem import TemperatureSensorItem
from ...model.item.sensors.VoltageSensorItem import VoltageSensorItem
from ..DiagramField.DiagramView import DiagramView, TimeDiagram, DualDiagram, BarDiagram, ThreeDimDiagram
from .DiagramItemView import DiagramItemView
from .OperatorItemView import OperatorItemView
from .SensorItemView import SensorItemView
from .WorkspaceItemView import WorkspaceItemView
from ...model.item.diagrams.WriteToFileItem import WriteToFileItem


class ItemEnumMeta(type(ABC), type(Enum)):
    pass


@unique
class ItemEnum(ABC, Enum, metaclass=ItemEnumMeta):
    def __init__(self, view: Type[WorkspaceItemView], color: str, model: Type[ItemModel], file: str):
        self.__view: Type[WorkspaceItemView] = view
        self.__color: str = color
        self.__model: Type[ItemModel] = model
        self.__path: str = SystemInfo.RESOURCES + 'images/items/' + file + '.svg'

    @property
    def model(self) -> Type[ItemModel]:
        return self.__model

    @property
    def path(self) -> str:
        return self.__path

    @property
    def background_color(self) -> str:
        return self.__color

    def create_workspace_item(self, parent: QWidget) -> WorkspaceItemView:
        return self.__view(parent, self)


@unique
class SensorEnum(ItemEnum):
    PROXY_SENSOR = (ProxySensorItem, 'file_read')
    CONSTANT = (ConstantItem, 'constant')
    NATURE_CONSTANT = (NatureConstantItem, 'nature_constant')
    TEMPERATURE_SENSOR = (TemperatureSensorItem, 'temperature')
    FORCE_SENSOR = (ForceSensorItem, 'force')
    DISTANCE_SENSOR = (DistanceSensorItem, 'distance')
    ACCELERATION_SENSOR = (AccelerationSensorItem, 'acceleration')
    CURRENT_SENSOR = (CurrentSensorItem, 'current')
    RGB_SENSOR = (RGBSensorItem, 'rgb')
    VOLTAGE_SENSOR = (VoltageSensorItem, 'voltage')

    def __init__(self, model: Type[SensorItem], file: str):
        super().__init__(SensorItemView, "#999999", model, 'sensor/' + file)


@unique
class OperatorEnum(ItemEnum):
    ADDITION_OPERATOR = (AdditionOperatorItem, 'addition')
    SUBTRACTION_OPERATOR = (SubtractionOperatorItem, 'subtraction')
    MULTIPLICATION_OPERATOR = (MultiplicationOperatorItem, 'multiplication')
    DIVISION_OPERATOR = (DivisionOperatorItem, 'division')
    ABSOLUTE_OPERATOR = (AbsoluteOperatorItem, 'absolute')
    NEGATIVE_OPERATOR = (NegativeOperatorItem, 'negative')
    POWER_OPERATOR = (PowerOperatorItem, 'power')
    POWER_TEN_OPERATOR = (MagnitudeOperatorItem, 'magnitude')
    ROOT_OPERATOR = (RootOperatorItem, 'root')
    CLONE_OPERATOR = (CloneItem, 'clone')

    def __init__(self, model: Type[OperatorItem], file: str):
        super().__init__(OperatorItemView, "#BBBBBB", model, 'operator/' + file)


@unique
class DiagramEnum(ItemEnum):
    WRITE_TO_FILE = (WriteToFileItem, 'file_write', None)
    TIME_DIAGRAM = (TimeDiagramItem, 'time', TimeDiagram)
    DUAL_DIAGRAM = (DualDiagramItem, 'dual', DualDiagram)
    BAR_DIAGRAM = (BarDiagramItem, 'bar', BarDiagram)
    THREE_DIM_DIAGRAM = (ThreeDimDiagramItem, 'three_dim', ThreeDimDiagram)

    def __init__(self, model: Type[DiagramItem], file: str, diagram: Type[DiagramView]):
        self.__diagram: Type[DiagramView] = diagram
        super().__init__(DiagramItemView, "#DDDDDD", model, 'diagram/' + file)

    @property
    def diagram(self) -> Type[DiagramView]:
        return self.__diagram
