import csv
import simplejson as json
import os
import quandl
import sys

def get_scrip_details(scrip_name):
    path = "data" + os.path.sep + "bse.csv"
    with open("data/bse.csv") as f:
        reader = csv.DictReader(f)

        for row in reader:
            if row['Security Id'] == scrip_name:
                return row

    return ""

def bse_price(bot, update):
    message = update.message.text
    name = message.split(" ")

    if len(name) == 1:
        bot.send_message(chat_id=update.message.chat_id,
                         text="Security name was not sent. Send the command again with a security name.")

    else:
        security_name = "".join(message.split(" ")[1:])
        security_name = security_name.upper().strip()
        scrip_details = get_scrip_details(security_name)

        if type(scrip_details) is dict:
            group = scrip_details["Group"]
            security_code = scrip_details['Security Code']
            face_value = scrip_details['Face Value']
            inr = float(scrip_details['INR'])
            industry = scrip_details['Industry']

            get = "{}/{}".format("NSE", security_name)

            quandl_token = os.environ["QUANDL_API_KEY"]
            try:

                df = quandl.get(get, authtoken=quandl_token, rows=1)
                parsed_json = json.loads(df.to_json())

                op = parsed_json["Open"]
                hg = parsed_json["High"]
                lw = parsed_json["Low"]
                la = parsed_json["Last"]

                open = op[op.keys()[0]]
                low = lw[lw.keys()[0]]
                high = hg[hg.keys()[0]]
                last = la[la.keys()[0]]

                reply = "<b> " + "{} price".format(security_name) + "</b>\n"

                reply = reply + "<pre>" + "Group:\t" + group + "\n"
                reply = reply + "Face value:\t" + face_value + "\n"
                reply = reply + "INR during scraping:\t" + str(inr) + "\n"
                reply = reply + "Industry:\t" + industry + "" + "</pre>" + "\n"
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



                print type(reply)
                print reply

                bot.send_message(chat_id=update.message.chat_id, text=reply, parse_mode="HTML")
            except:
                bot.send_message(chat_id=update.message.chat_id,
                                 text="Error occured. Check log for details")
                raise
                sys.exit(0)
        else:
            bot.send_message(chat_id=update.message.chat_id,
                             text="Check scrip name and try again.")
