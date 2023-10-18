import copy
import random
from typing import List


class Region:
    # LPL = "LPL"
    # LCK = "LCK"
    # LEC = "LEC"
    # LCS = "LCS"
    # VCS = "VCS"
    East = "East"
    West = "West"
    G2 = "G2"


class Team:
    wins = 0
    loss = 0

    def __init__(self, name: str, region: str):
        self.name = name
        self.region = region

    def __str__(self):
        return f"{self.name}"
        # return f"{self.name} Win/Loss: {self.wins} - {self.loss}"


def RuleBook(first: Team, second):
    # same region random
    if first.region == second.region:
        return random.randint(0, 1)

    # always east win vs everyone
    if first.region == Region.East:
        return 0

    if second.region == Region.East:
        return 1

    if first.region == Region.G2:
        return 0
    if second.region == Region.G2:
        return 1

    return random.randint(0, 1)


class Match:
    winner = None
    loser = None

    def __init__(self, first: Team, second: Team):
        self.firstteam = first
        self.secondteam = second

    def setWinner(self, winner):
        if winner == 0:
            self.winner = self.firstteam
            self.loser = self.secondteam
            self.firstteam.wins += 1
            self.secondteam.loss += 1
        if winner == 1:
            self.winner = self.secondteam
            self.loser = self.firstteam
            self.secondteam.wins += 1
            self.firstteam.loss += 1

    def __str__(self):
        if self.winner != None and self.loser != None:
            return f"{self.firstteam} vs {self.secondteam} winner:{self.winner.name}"
        else:
            return f"{self.firstteam} vs {self.secondteam}"


class Round:
    complete = False
    matchList = []
    teamPlaying = []
    win = -1
    loss = -1

    def __init__(self, matchesToAdd: Match):
        self.matchList: List[Match] = matchesToAdd
        self.teamPlaying: Team = []

    def insertMatch(self, matches: List[Match]):
        if len(matches) != 0:
            for i in range(0, len(matches)):
                self.matchList.append(matches[i])

    def insertTeams(self, teamsToInsert: Team):
        if len(teamsToInsert) != 0:
            for i in range(0, len(teamsToInsert)):
                self.teamPlaying.append(teamsToInsert[i])
                self.win = teamsToInsert[i].wins
                self.loss = teamsToInsert[i].loss

    def makeComplete(self):
        self.complete = True

    def __str__(self):
        s = f"Round: {self.win} - {self.loss}\n --------- \n"

        for i in range(0, len(self.matchList)):
            s = s + f"{str(self.matchList[i])}" + "\n"
        return s


class Tournament:
    roundList = []

    def __init__(self, teamList: Team):
        self.teamList = teamList
        matchList = [
            Match(t1, tl),
            Match(c9, mad),
            Match(geng, gam),
            Match(jdg, bds),
            Match(g2, dwg),
            Match(nrg, wbg),
            Match(fnc, lng),
            Match(blg, kt),
        ]
        tempRound = Round(matchList)
        tempRound.insertTeams(
            [
                t1,
                tl,
                c9,
                mad,
                geng,
                gam,
                jdg,
                bds,
                g2,
                dwg,
                nrg,
                wbg,
                fnc,
                lng,
                blg,
                kt,
            ]
        )
        self.roundList.append(tempRound)

    def generateNextRound(self):
        tempList = []
        for i in range(0, len(self.roundList)):
            temp: Round = self.roundList[i]
            if temp.complete == True:
                continue

            upper: Team = []
            lower: Team = []
            for i in range(0, len(temp.matchList)):
                # rd = RuleBook(temp.matchList[i].firstteam, temp.matchList[i].secondteam)
                print(f"Round {temp.win} - {temp.loss}")
                print(temp.matchList[i])
                rd = int(input())
                temp.matchList[i].setWinner(rd)
                if temp.matchList[i].winner.wins < 3:
                    upper.append(temp.matchList[i].winner)
                elif temp.matchList[i].winner.wins == 3:
                    qualified.append(temp.matchList[i].winner)
                if temp.matchList[i].loser.loss < 3:
                    lower.append(temp.matchList[i].loser)
                elif temp.matchList[i].loser.loss == 3:
                    disqualified.append(temp.matchList[i].loser)

            upperRound: Round = Round([])
            upperSwap = True
            upperIndex = -1
            lowerRound: Round = Round([])
            lowerSwap = True
            lowerIndex = -1

            if len(upper) != 0:
                for i in range(0, len(tempList)):
                    if (
                        tempList[i].win == upper[0].wins
                        and tempList[i].loss == upper[0].loss
                    ):
                        upperIndex = i
                        upperSwap = False
                        break

                if len(upper) != 0 and upperSwap:
                    upperRound.insertTeams(upper)
                    tempList.append(upperRound)
                elif len(upper) != 0 and (not upperSwap):
                    tempList[upperIndex].insertTeams(upper)

            if len(lower) != 0:
                for i in range(0, len(tempList)):
                    if (
                        tempList[i].win == lower[0].wins
                        and tempList[i].loss == lower[0].loss
                    ):
                        lowerIndex = i
                        lowerSwap = False
                        break

                if len(lower) != 0 and lowerSwap:
                    lowerRound.insertTeams(lower)
                    tempList.append(lowerRound)
                elif len(lower) != 0 and (not lowerSwap):
                    tempList[lowerIndex].insertTeams(lower)

            temp.makeComplete()

        for i in range(0, len(tempList)):
            current = tempList[i].teamPlaying
            random.shuffle(current)
            for j in range(0, len(current), 2):
                tempList[i].insertMatch([Match(current[j], current[j + 1])])

        for i in range(0, len(tempList)):
            self.roundList.append(tempList[i])


if __name__ == "__main__":
    westCount = 0
    noGames = 1000
    gameType = 0
    if gameType == 0:
        blg = Team("BLG", Region.East)
        c9 = Team("C9", Region.West)
        dwg = Team("DWG", Region.East)
        fnc = Team("FNC", Region.West)
        g2 = Team("G2", Region.G2)
        gam = Team("GAM", Region.West)
        geng = Team("GENG", Region.East)
        jdg = Team("JDG", Region.East)
        kt = Team("KT", Region.East)
        lng = Team("LNG", Region.East)
        mad = Team("MAD", Region.West)
        nrg = Team("NRG", Region.West)
        t1 = Team("T1", Region.East)
        bds = Team("BDS", Region.West)
        tl = Team("TL", Region.West)
        wbg = Team("WBG", Region.East)
        teams = [
            blg,
            c9,
            dwg,
            fnc,
            g2,
            gam,
            geng,
            jdg,
            kt,
            lng,
            mad,
            nrg,
            t1,
            bds,
            tl,
            wbg,
        ]
        tourney = Tournament(teams)
        qualified = []
        disqualified = []
        # Round 1
        tourney.generateNextRound()
        # Round 2
        tourney.generateNextRound()
        # Round 3
        tourney.generateNextRound()
        # Round 4
        tourney.generateNextRound()
        # Round 5
        tourney.generateNextRound()

        for i in range(0, len(tourney.roundList)):
            print(tourney.roundList[i])
            print("\n")

        print("Qualified")
        for i in range(0, len(qualified)):
            print(f"{qualified[i]}")

        print("\nDisqualified")
        for i in range(0, len(disqualified)):
            print(f"{disqualified[i]}")

    else:
        for i in range(0, noGames):
            blg = Team("BLG", Region.East)
            c9 = Team("C9", Region.West)
            dwg = Team("DWG", Region.East)
            fnc = Team("FNC", Region.West)
            g2 = Team("G2", Region.G2)
            gam = Team("GAM", Region.West)
            geng = Team("GENG", Region.East)
            jdg = Team("JDG", Region.East)
            kt = Team("KT", Region.East)
            lng = Team("LNG", Region.East)
            mad = Team("MAD", Region.West)
            nrg = Team("NRG", Region.West)
            t1 = Team("T1", Region.East)
            bds = Team("BDS", Region.West)
            tl = Team("TL", Region.West)
            wbg = Team("WBG", Region.East)
            teams = [
                blg,
                c9,
                dwg,
                fnc,
                g2,
                gam,
                geng,
                jdg,
                kt,
                lng,
                mad,
                nrg,
                t1,
                bds,
                tl,
                wbg,
            ]
            print(i)
            tourney = Tournament(teams)
            qualified = []
            disqualified = []
            # Round 1
            tourney.generateNextRound()
            # Round 2
            tourney.generateNextRound()
            # Round 3
            tourney.generateNextRound()
            # Round 4
            tourney.generateNextRound()
            # Round 5
            tourney.generateNextRound()

            for j in range(0, len(qualified)):
                if (
                    qualified[j].region == Region.West
                    or qualified[j].region == Region.G2
                ):
                    westCount += 1
            del tourney
            del (
                blg,
                c9,
                dwg,
                fnc,
                g2,
                gam,
                geng,
                jdg,
                kt,
                lng,
                mad,
                nrg,
                t1,
                bds,
                tl,
                wbg,
            )

        print(f"Probability of West Qualifying {westCount/noGames}")
