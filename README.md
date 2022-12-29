# Password Generator
A simple command-line tool for generating passwords.

## Installation
To install the PasswordGenerator library, run the following command:

`pip install password-generator`

## Usage
To generate a password with the default options (length: 16, special characters: False), run the following command:

`password-generator`

To generate a password with specific options, use the following command-line arguments:
* -l or --length: The length of the generated password (default: 16).
* -s or --special-chars: Whether to include special characters in the generated password (default: False).
For example, to generate a password with a length of 32 and special characters, run the following command:

`password-generator -l 32 -s`

## Dependencies
This library has the following external dependencies:
* secrets - A Python standard library module for generating secure random numbers.

## License
This library is licensed under the MIT License. See the LICENSE file for more information.
