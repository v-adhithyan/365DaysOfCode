import csv
import os

def add_stock(bot, update):
    message = update.message.text
    contents = message.split(" ")

    if len(contents) <= 4:
        bot.send_message(chat_id=update.message.chat_id,
                         text="Send scrip name followed by quantity and price and other charges. For example if you bought GMR INFRA 100 shares each at 20"
                              + " INR with 100 brokerage send: <pre> GMRINFRA 100 20 100 </pre>", parse_mode="HTML")

    else:
        try:
            #values = contents.split(" ")
            scrip_name = str(contents[1]).upper()
            quantity = float(contents[2])
            cost_price = float(contents[3])
            brokerage = float(contents[4])

            row = {}
            row['Security Name'] = scrip_name
            row['Quantity'] = quantity
            row["Cost Price"] = cost_price
            row["Brokerage"] = brokerage
            row["Total"] = (quantity*cost_price) + brokerage
            data = [row]
            file = "data" + os.path.sep + "portfolio.csv"

            if not os.path.exists(file):
                with open(file, "w") as f:
                    writer = csv.DictWriter(f, fieldnames=row.keys())
                    writer.writeheader()
                    writer.writerow(row)
            else:
                with open(file, "a") as f:
                    writer = csv.DictWriter(f, fieldnames=row.keys())
                    writer.writerow(row)

            bot.send_message(chat_id=update.message.chat_id, text="Added successfully :)")

        except:
            bot.send_message(chat_id=update.message.chat_id, text="Error occured. Check log for details.")
            raise