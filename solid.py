from abc import ABC, abstractmethod
class Netflix(ABC):
    def __init__(self, username, pwd, device):
        self.username = username
        self.pwd = pwd
        self.save_device = device
class ContentManager(Netflix):
    @abstractmethod
    def play(self):
        pass
class Downloadable(Netflix):
    @abstractmethod
    def download(self):
        pass
class Movies(ContentManager, Downloadable):
    def __init__(self, username, pwd, device):
        super().__init__(username, pwd, device)
    def play(self):
        print("Playing a movie!")
    def download(self):
        print(f"Downloading the movie to {self.save_device.__class__.__name__}")
class Series(ContentManager, Downloadable):
    def __init__(self, username, pwd, device):
        super().__init__(username, pwd, device)
    def play(self):
        print("Playing a Series!")
    def upload(self):
        print("Uploading a new Season!!")
    def next(self):
        print("Playing next episode.")
    def prev(self):
        print("Previous Episode.")
    def download(self):
        print(f"Downloading the series!! {self.save_device.__class__.__name__}")
        print("Previous Episode.")
class Documentary(ContentManager, Downloadable):
    def __init__(self, username, pwd, device):
        super().__init__(username, pwd, device)
    def play(self):
        print("Playing a Documentary!")
    def download(self):
        print(f"Downloading the documentary!!{self.save_device.__class__.__name__}")
class Trailer(ContentManager):
    def play(self):
        print("Playing a Trailer!")
class PaymentManager(Netflix):
    @abstractmethod
    def pay(self):
        pass
class NotificationManager(Netflix):
    @abstractmethod
    def notify(self):
        pass
class Device(ABC):
    @abstractmethod
    def save(self):
        pass
class Phone(Device):
    def save(self):
        print("Saving data to your phone.")
class Tablet(Device):
    def save(self):
        print("Saving data to your tablet.")
class Desktop(Device):
    def save(self):
        print("Saving data to your desktop.")
class TV(Device):
    def save(self):
        print("Saving data to your tv.")
def play_content(content):
    content.play()
movie = Movies("alice123", 123, TV())
play_content(movie)
play_content(Series("alice123", 123, Desktop()))
play_content(Documentary("alice123", 123, TV()))
play_content(Trailer("alice123", 123, Tablet()))
movie.download()

# Design a banking system with: • An abstract base class Account with deposit(), withdraw(), calculate_interest().
# • Subclasses: SavingsAccount, CurrentAccount, FixedDepositAccount.
# • Each account must: o Encapsulate balance (private)
# o Provide controlled access through properties
# o Override interest calculation differently
# • Include a static method to validate amount.
# • Include a class method to update bank-wide interest policies.

from abc import ABC, abstractmethod
class banking_system(ABC):
    def __init__(self,):
