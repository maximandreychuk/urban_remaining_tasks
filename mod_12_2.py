from unittest import TestCase


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = str(participant)
                    place += 1
                    self.participants.remove(participant)

        return finishers


class TournamentTest(TestCase):
    def setUp(self):
        self.runner1 = Runner(name="Усэйн", speed=10)
        self.runner2 = Runner(name="Андрей", speed=9)
        self.runner3 = Runner(name="Ник", speed=3)

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @classmethod
    def tearDownClass(cls):
        for dct in reversed(cls.all_results.values()):
            print(dct)

    def test_runner_1_with_runner_3(self):
        turik = Tournament(90, self.runner1, self.runner3)
        all_results = turik.start()
        msg = "Test value is not true."
        self.assertTrue(list(all_results.values())[-1] == self.runner3, msg)
        self.all_results["1"] = all_results

    def test_runner_2_with_runner_3(self):
        turik = Tournament(90, self.runner2, self.runner3)
        all_results = turik.start()
        msg = "Test value is not true."
        self.assertTrue(list(all_results.values())[-1] == self.runner3, msg)
        self.all_results["2"] = all_results

    def test_runner_1_with_runner_2_with_runner_3(self):
        turik = Tournament(90, self.runner1, self.runner2, self.runner3)
        all_results = turik.start()
        msg = "Test value is not true."
        self.assertTrue(list(all_results.values())[-1] == self.runner3, msg)
        self.all_results["3"] = all_results
