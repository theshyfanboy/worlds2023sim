import { React, useEffect, useState } from 'react';
import styles from '../../styles/Home.module.css';
import Image from 'next/image'
import vsimage from '../../public/teams/vs.png';

export default function Round({ roundHistory, actionButton, roundStatus }) {
    const [choices, setChoices] = useState([]);

    const addChoice = (match, pick, roundwin, roundloss) => {
        console.log(roundloss, roundwin)
        var foundIndex = -1
        if (choices.length != 0) {
            foundIndex = choices.findIndex(obj => obj.cMatch.firstteam.name == match.firstteam.name && obj.cMatch.secondteam.name == match.secondteam.name && obj.roundwin == roundwin && obj.roundloss == roundloss)
        }

        if (foundIndex !== -1) {
            const newTemp = [...choices]
            newTemp[foundIndex].picked = pick
            setChoices(newTemp);
        } else {
            const temp = {
                cMatch: match,
                picked: pick,
                roundwin: roundwin,
                roundloss: roundloss,
            }
            const newTemp = [...choices, temp]
            setChoices(newTemp);
        }
    }

    return <div className={styles.round} >
        {roundHistory.map((round) =>
            <div>
                <div className={styles.subround}>
                    <div className={styles.head}>
                        <div className={styles.headTitle}>
                            {round.win} - {round.loss}
                        </div>
                    </div>
                    <div>
                        {round.matchList.map((match) => {
                            return <div className={styles.match}>
                                {match.winner == match.firstteam ?
                                    <div onClick={() => { addChoice(match, 0, round.win, round.loss) }} className={styles.winner}>
                                        <Image width={65} src={match.firstteam.image} alt={match.firstteam.name} />
                                    </div>
                                    :
                                    choices.findIndex(obj => obj.cMatch.firstteam.name == match.firstteam.name && obj.cMatch.secondteam.name == match.secondteam.name && parseInt(obj.picked) == 0) !== -1 && match.winner != match.secondteam ?
                                        <div onClick={() => { addChoice(match, 0, round.win, round.loss) }} className={styles.winner}>
                                            <Image width={65} src={match.firstteam.image} alt={match.firstteam.name} />
                                        </div>
                                        :
                                        <div onClick={() => { addChoice(match, 0, round.win, round.loss) }} className={styles.selecting}>
                                            <Image width={65} src={match.firstteam.image} alt={match.firstteam.name} />
                                        </div>
                                }
                                <div className={styles.vsPad}>
                                    <Image width={40} src={vsimage} alt="vs" />
                                </div>
                                {match.winner == match.secondteam ?
                                    <div onClick={() => { addChoice(match, 1, round.win, round.loss) }} className={styles.winner}>
                                        <Image width={65} src={match.secondteam.image} alt={match.secondteam.name} />
                                    </div>
                                    :
                                    choices.findIndex(obj => obj.cMatch.firstteam.name == match.firstteam.name && obj.cMatch.secondteam.name == match.secondteam.name && parseInt(obj.picked) == 1) !== -1 && match.winner != match.firstteam ?
                                        <div onClick={() => { addChoice(match, 1, round.win, round.loss) }} className={styles.winner}>
                                            <Image width={65} src={match.secondteam.image} alt={match.secondteam.name} />
                                        </div>
                                        :
                                        <div onClick={() => { addChoice(match, 1, round.win, round.loss) }} className={styles.selecting}>
                                            <Image width={65} src={match.secondteam.image} alt={match.secondteam.name} />
                                        </div>
                                }
                            </div>
                        }
                        )}
                    </div>
                </div>
            </div>

        )}

        {!roundStatus ? <div className={styles.lockButtonContainer}>
            <button onClick={() => { actionButton(choices); }} className={styles.lockButton}>Lock in</button>
        </div> : <></>}
    </div >
}
