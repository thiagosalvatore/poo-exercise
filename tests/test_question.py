import pytest

from poo_exercise.models import Question


def test_create_question():
    question = Question("Whats your name", ["Thiago", "James", "Bond"], "Thiago")
    assert question


def test_create_question_without_options_should_raise_error():
    with pytest.raises(AssertionError):
        Question("Whats your name", [], None)


def test_create_question_invalid_correct_value_should_raise_error():
    with pytest.raises(AssertionError):
        Question("Whats your name", ["Thiago", "James", "Bond"], "Joao")
