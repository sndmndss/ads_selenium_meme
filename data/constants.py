OPEN_URL = "http://local.adspower.net:50325/api/v1/browser/start?serial_number="
OPEN_URL_ID = "http://local.adspower.net:50325/api/v1/browser/start?user_id="
CLOSE_URL = "http://local.adspower.net:50325/api/v1/browser/stop?serial_number="
CLOSE_URL_ID = "http://local.adspower.net:50325/api/v1/browser/stop?user_id="
DISCORD = "https://discord.com/login"
RABBY_URL = "chrome-extension://acmacodkjbdgmoleebolmdjonilkdbch/index.html#/no-address"
API_URL = "http://local.adspower.net:50325"
DYNO_MEME = "https://dyno.gg/auth?return=/form/cba26bfa"
MEME_FARMING = "https://www.memecoin.org/farming"
RAINBOW_LINK = "chrome-extension://opfgelmcmbiajamepnmloijbpoleiama/popup.html#/import/pkey?onboarding=true"
MOLLY_LINK = "https://app.mollygateway.com/profile/qorr10ubrq4yvtgcvcylv"
BERACHAIN = "https://app.mvhq.io/missions/berachain-farming-vol1"
TWITTER_LINK = "https://twitter.com/"
GMAIL_LINK = "https://www.google.com/intl/ua/gmail/about/"
js_code_discord = """
        function login(token) {
        setInterval(() => {
            document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`
        }, 50);
        setTimeout(() => {
            location.reload();
        }, 2500);
    }
        login(arguments[0]);
            """
