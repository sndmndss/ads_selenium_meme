OPEN_URL = "http://local.adspower.net:50325/api/v1/browser/start?serial_number="
CLOSE_URL = "http://local.adspower.net:50325/api/v1/browser/stop?serial_number="
DISCORD_MEME = "https://discord.com/invite/memeland"
API_KEY = "6c3a65d84edfb8c92cb2c43faf01db0b"
API_URL = "http://local.adspower.net:50325"
DYNO_MEME = "https://dyno.gg/auth?return=/form/ecfaebc1"
MEME_FARMING = "https://www.memecoin.org/farming"
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
