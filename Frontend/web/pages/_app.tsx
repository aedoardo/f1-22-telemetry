import '../styles/globals.css'
import type { AppProps } from 'next/app'
import localFont from '@next/font/local';

const myFont = localFont({src: '../fonts/regularwebf1.ttf'});

export default function App({ Component, pageProps }: AppProps) {
  return (
    <main style={{width: "100%", height: "100%"}} className={myFont.className}>
      <Component {...pageProps} />
    </main>
  )
}
