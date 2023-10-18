import Head from 'next/head';
import styles from '../styles/Home.module.css';
import RandomizedBracket from './randomizedBracket';

export default function Home() {
  return (
    <div className={styles.container}>
      <Head>
        <title>Worlds 2023 Swiss Stage</title>
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <RandomizedBracket></RandomizedBracket>
    </div>
  );
}