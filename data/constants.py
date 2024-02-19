OPEN_URL = "http://local.adspower.net:50325/api/v1/browser/start?serial_number="
CLOSE_URL = "http://local.adspower.net:50325/api/v1/browser/stop?serial_number="
DISCORD = "https://discord.com/login"
API_URL = "http://local.adspower.net:50325"
DYNO_MEME = "https://dyno.gg/auth?return=/form/cba26bfa"
MEME_FARMING = "https://www.memecoin.org/farming"
RAINBOW_LINK = "chrome-extension://opfgelmcmbiajamepnmloijbpoleiama/popup.html#/import/pkey?onboarding=true"
MOLLY_LINK = "https://app.mollygateway.com/profile/qorr10ubrq4yvtgcvcylv"
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
