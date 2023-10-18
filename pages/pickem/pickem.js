import PickemBracket from './pickemBracket'
import styles from '../../styles/Home.module.css';

export default function PickemPlay() {
    return (
        <div className={styles.container}>
            <PickemBracket></PickemBracket>
        </div>
    );
}