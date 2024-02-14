OPEN_URL = "http://local.adspower.net:50325/api/v1/browser/start?serial_number="
CLOSE_URL = "http://local.adspower.net:50325/api/v1/browser/stop?serial_number="
DISCORD_MEME = "https://discord.com/invite/memeland"
API_URL = "http://local.adspower.net:50325"
DYNO_MEME = "https://dyno.gg/auth?return=/form/ecfaebc1"
MEME_FARMING = "https://www.memecoin.org/farming"
RAINBOW_LINK = "chrome-extension://opfgelmcmbiajamepnmloijbpoleiama/popup.html#/import/pkey?onboarding=true"
js_code = """
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
