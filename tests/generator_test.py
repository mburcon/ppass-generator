import string

from new_pass.generator import PasswordGenerator


def test_generate():
    generator = PasswordGenerator()
    password = generator.generate()

    # Test that the generated password is the correct length
    assert len(password) == 16

    # Test that the generated password only contains ASCII letters and digits
    assert all(c in string.ascii_letters + string.digits for c in password)


def test_generate_length():
    generator = PasswordGenerator(length=32)
    password = generator.generate()

    # Test that the generated password is the correct length
    assert len(password) == 32

    # Test that the generated password only contains ASCII letters and digits
    assert all(c in string.ascii_letters + string.digits for c in password)


def test_generate_special_chars():
    generator = PasswordGenerator(special_chars=True)
    password = generator.generate()

    # Test that the generated password is the correct length
    assert len(password) == 16

    # Test that the generated password contains ASCII letters, digits, and special characters
    assert any(c in string.punctuation for c in password)


def test_generate_length_special_chars():
    generator = PasswordGenerator(length=32, special_chars=True)
    password = generator.generate()

    # Test that the generated password is the correct length
    assert len(password) == 32

    # Test that the generated password contains ASCII letters, digits, and special characters
    assert any(c in string.punctuation for c in password)
