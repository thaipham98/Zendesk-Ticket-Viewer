import pytest
from unittest.mock import Mock, patch
import requests
from requests.models import HTTPError
from api import validate_response, get_all_tickets, get_ticket_detail, get_paging, get_total_page

@patch('requests.get')
def test_validate_response__error_status_code__raise_http_error(mock_get):
    mock_get.return_value = Mock(status_code=500, reason="API unavailable", json={})
    with pytest.raises(HTTPError):
        validate_response(mock_get.return_value)

  
@patch('requests.get')
def test_validate_response__successful_status_code__pass(mock_get):
    mock_get.return_value = Mock(status_code=200, reason="API is good", json={})
    validate_response(mock_get.return_value)

@patch('requests.get')
def test_get_ticket_detail__valid_ticket_id(mock_get):
    ticket_id = 5
    mock_get.return_value = Mock(status_code=200, reason="API is good", json={"ticket_id": ticket_id})
    mock_get.return_value.text = '{"ticket_id": 5}'
    response = get_ticket_detail(ticket_id)
    assert response["ticket_id"] == ticket_id

