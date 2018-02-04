import urllib2
import simplejson as json
import os
import quandl

def nse_price(bot, update):
    message = update.message.text
    name = message.split(" ")

    if len(name) == 1:
        bot.send_message(chat_id=update.message.chat_id, text="Security name was not sent. Send the command again with a security name.")

    else:
        security_name = "".join(message.split(" ")[1:])
        security_name = security_name.upper().strip()
        print security_name
        get = "{}/{}".format("NSE", security_name)

        quandl_token = os.environ["QUANDL_API_KEY"]
        try:

            df = quandl.get(get, authtoken=quandl_token, rows=1)
            parsed_json = json.loads(df.to_json())

            op =parsed_json["Open"]
            hg = parsed_json["High"]
            lw = parsed_json["Low"]
            la = parsed_json["Last"]

            open = op[op.keys()[0]]
            low = lw[lw.keys()[0]]
            high = hg[hg.keys()[0]]
            last = la[la.keys()[0]]

            reply = "<b> " + "{} price".format(security_name) + "</b>\n"
            reply = reply + "Open\t{}\n".format(open)
            reply = reply + "High\t{}\n".format(high)
            reply = reply + "Low\t{}\n".format(low)
            reply = reply + "LTP\t{}\n".format(last)


            if last > open:
                msg = "Up by {}".format(last - open)
                reply = reply + "{} {} {} {}".format("<b>", msg, "</b>", "\n")
            elif last < open:
                msg = "Down by {}".format(last - open)
                reply = reply + "{} {} {} {}".format("<i>", msg, "</i>", "\n")
            else:
                msg = "No change in price"
                reply = reply + "{} {} {} {}".format("", msg, "", "\n")

            print type(reply)
            print reply

            bot.send_message(chat_id=update.message.chat_id, text = reply, parse_mode="HTML")
        except:
            bot.send_message(chat_id=update.message.chat_id,
                             text="Incorrect security name. Send correct name.")
            raise
