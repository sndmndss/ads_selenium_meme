OPEN_URL = "http://local.adspower.net:50325/api/v1/browser/start?serial_number="
CLOSE_URL = "http://local.adspower.net:50325/api/v1/browser/stop?serial_number="
DISCORD_MEME = "https://discord.com/invite/memeland"
API_URL = "http://local.adspower.net:50325"
DYNO_MEME = "https://dyno.gg/auth?return=/form/ecfaebc1"
MEME_FARMING = "https://www.memecoin.org/farming"
RAINBOW_LINK = "chrome-extension://opfgelmcmbiajamepnmloijbpoleiama/popup.html#/import/pkey?onboarding=true"
RAINBOW_INPUT_CSS_SELECTOR = ("#main > div > div._28iyjl0._28iyjl5u._28iyjliy.lt-dc.dt-dc > div > div:nth-child(1) "
                              "> div > div > div > div._28iyjl0._28iyjlf0._28iyjlg7 > "
                              "div._28iyjl0._28iyjl6g._28iyjl6k._28iyjl4z._28iyjl7c > div._28iyjl0._28iyjlie > "
                              "div > div > input")
RAINBOW_BUTTON_CSS_SELECTOR = ("#main > div > div._28iyjl0._28iyjl5u._28iyjliy.lt-dc.dt-dc > div > div:nth-child(1) "
                               "> div > div > div > div._28iyjl0._28iyjlf0._28iyjlg7 > "
                               "div._28iyjl0._28iyjlie._28iyjlh7._28iyjldt > div > button")
RAINBOW_PASSWORD_1 = ("#main > div > div._28iyjl0._28iyjl5u._28iyjliy.lt-dc.dt-dc > div > div:nth-child(1) > div > div > "
                      "div > div._28iyjl0._28iyjlf0._28iyjlg7._28iyjl6g._28iyjl6k._28iyjl4z > div > div:nth-child(1)"
                      " > div._28iyjl0._28iyjlhg._28iyjlie > div > div:nth-child(1) > div > div:nth-child(2) > div "
                      "> div._28iyjl80._28iyjlie > input")
RAINBOW_PASSWORD_2 = ("#main > div > div._28iyjl0._28iyjl5u._28iyjliy.lt-dc.dt-dc > div > div:nth-child(1) > div"
                      " > div > div > div._28iyjl0._28iyjlf0._28iyjlg7._28iyjl6g._28iyjl6k._28iyjl4z > "
                      "div > div:nth-child(1) > div._28iyjl0._28iyjlhg._28iyjlie > div > div:nth-child(2) "
                      "> div > div:nth-child(2) > div > div:nth-child(1) > div > div._28iyjl80._28iyjlie > input")
RAINBOW_BUTTON_2_CSS_SELECTOR = ("#main > div > div._28iyjl0._28iyjl5u._28iyjliy.lt-dc.dt-dc > div > div:nth-child(1) > "
                                 "div > div > div > div._28iyjl0._28iyjlf0._28iyjlg7._28iyjl6g._28iyjl6k._28iyjl4z >"
                                 " div > div:nth-child(2) > div > div > div:nth-child(2) > div > button")
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
