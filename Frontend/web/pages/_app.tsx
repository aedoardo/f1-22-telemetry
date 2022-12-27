import '../styles/globals.css'
import type { AppProps } from 'next/app'
import localFont from '@next/font/local';
import { wrapper } from "../store/store";

const myFont = localFont({src: '../fonts/regularwebf1.ttf'});

function App({ Component, pageProps }: AppProps) {
  return (
    <main style={{width: "100%", height: "100%"}} className={myFont.className}>
      <Component {...pageProps} />
    </main>
  )
}

export default wrapper.withRedux(App);
