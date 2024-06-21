import pytest
from datetime import datetime
from helpers import check_scheduled_time, pause_for_60_minutes
from airflow.exceptions import AirflowException

def test_check_scheduled_time_success(mocker):
    # Arrange
    mock_datetime = mocker.patch('helpers.datetime')
    mock_logger = mocker.patch('helpers.LOGGER')
    mock_datetime.now.return_value = datetime.strptime('14:00', '%H:%M')
    times = ['14:00']
    
    # Act
    check_scheduled_time(times)
    
    # Assert
    mock_logger.info.assert_called_with("Current time: 14:00 matches scheduled time: 14:00, allowing task to proceed...")

def test_check_scheduled_time_failure(mocker):
    # Arrange
    mock_datetime = mocker.patch('helpers.datetime')
    mock_datetime.now.return_value = datetime.strptime('14:00', '%H:%M')
    times = ['13:00']
    
    # Act & Assert
    with pytest.raises(AirflowException):
        check_scheduled_time(times)

def test_pause_for_60_minutes_prod(mocker):
    # Arrange
    mock_sleep = mocker.patch('helpers.time.sleep', return_value=None)
    env = 'prod'
    
    # Act
    pause_for_60_minutes(env)
    
    # Assert
    mock_sleep.assert_called_with(60 * 60)

def test_pause_for_60_minutes_non_prod(mocker):
    # Arrange
    mock_sleep = mocker.patch('helpers.time.sleep', return_value=None)
    env = 'dev'
    
    # Act
    pause_for_60_minutes(env)
    
    # Assert
    mock_sleep.assert_not_called()
