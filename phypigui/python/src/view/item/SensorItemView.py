from python.src.view.item.WorkspaceItemView import WorkspaceItemView


class SensorItemView(WorkspaceItemView):
    def __init__(self, parent, id: int, icon_path: str):
        super().__init__(parent, id, icon_path)
