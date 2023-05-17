import getpass
import re
import hashlib
import string

class PasswordChecker:
    def __init__(self, password):
        self.password = password

    def check_length(self):
        """Check if password length is at least 8."""
        return len(self.password) >= 8

    def check_digit(self):
        """Check if password contains at least one digit."""
        return any(character.isdigit() for character in self.password)

    def check_uppercase(self):
        """Check if password contains at least one uppercase letter."""
        return any(character.isupper() for character in self.password)

    def check_lowercase(self):
        """Check if password contains at least one lowercase letter."""
        return any(character.islower() for character in self.password)

    def check_special_char(self):
        """Check if password contains at least one special character."""
        return any(character in string.punctuation for character in self.password)

    def check_sequence(self):
        """Check if password contains a common sequence (e.g., "123", "abc")."""
        sequences = ["123", "abc", "password", "admin", "qwerty"]
        return not any(sequence in self.password for sequence in sequences)

    def check_repeated_char(self):
        """Check if password contains repeated characters."""
        return len(self.password) == len(set(self.password))

    def hash_password(self):
        """Hash the password using SHA256."""
        return hashlib.sha256(self.password.encode()).hexdigest()

    def check_strength(self):
        """Check overall password strength."""
        checks = [self.check_length(), self.check_digit(),
                  self.check_uppercase(), self.check_lowercase(),
                  self.check_special_char(), self.check_sequence(),
                  self.check_repeated_char()]

        if all(checks):
            return "Strong password"
        else:
            return "Weak password"

def main():
    password = getpass.getpass("Enter your password: ")
    checker = PasswordChecker(password)
    print(checker.check_strength())
    print("Hashed password:", checker.hash_password())

if __name__ == "__main__":
    main()
