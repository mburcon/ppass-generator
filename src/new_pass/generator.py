import argparse
import secrets
import string


class PasswordGenerator:
    def __init__(self, length=16, special_chars=False):
        self.length = length
        self.special_chars = special_chars

    def generate(self):
        """Generate a password."""
        # Determine the character set to use
        if self.special_chars:
            charset = string.ascii_letters + string.digits + string.punctuation
        else:
            charset = string.ascii_letters + string.digits

        # Generate the password
        password = "".join(secrets.choice(charset) for i in range(self.length))
        return password


def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Generate a password.")
    parser.add_argument(
        "-l",
        "--length",
        type=int,
        default=16,
        help="The length of the generated password (default: 16).",
    )
    parser.add_argument(
        "-s",
        "--special-chars",
        action="store_true",
        help="Whether to include special characters in the generated password.",
    )
    args = parser.parse_args()

    # Generate the password
    generator = PasswordGenerator(length=args.length, special_chars=args.special_chars)
    password = generator.generate()

    # Print the password
    print(password)


if __name__ == "__main__":
    main()
