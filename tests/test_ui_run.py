import types
from unittest import mock
import ui
import ui.side_by_side as side


def test_run_no_exceptions():
    fake_tk = types.SimpleNamespace()
    fake_tk.END = "end"
    fake_tk.Tk = mock.MagicMock(return_value=mock.MagicMock())
    fake_widget = mock.MagicMock(return_value=mock.MagicMock())
    fake_tk.Label = fake_widget
    fake_tk.Text = mock.MagicMock(return_value=mock.MagicMock(get=mock.MagicMock(return_value="")))
    fake_tk.Frame = fake_widget
    fake_tk.Button = fake_widget
    fake_tk.StringVar = mock.MagicMock(return_value=mock.MagicMock())

    with mock.patch.object(side, "tk", fake_tk):
        ui.run()
