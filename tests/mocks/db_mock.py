# tests/test_banco_controller.py
from unittest.mock import MagicMock, patch


@patch("src.database.banco_controller.get_connection")
def test_drop_database(mock_get_connection):
    mock_cursor = MagicMock()
    mock_conn = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    mock_get_connection.return_value.__enter__.return_value = mock_conn

    excluir_bancos("teste_banco")

    mock_cursor.execute.assert_called_once_with("DROP DATABASE [teste_banco]")
    mock_conn.commit.assert_called_once()
