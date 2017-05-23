import numpy as np


def run():
    num_funds = int(raw_input("Number of starting funds: "))
    fund_amounts = []
    for i in range(num_funds):
        amount_str = raw_input("Dollar amount in fund {}: ".format(i + 1))
        amount_str = amount_str.replace(",", "")
        fund_amounts.append(float(amount_str))
    total_amount = np.sum(fund_amounts)
    num_rebalanced_funds = int(raw_input("Number of rebalanced funds: "))

    rebalanced_amounts = []
    for i in range(num_rebalanced_funds):
        percentage = float(raw_input("Percentage (float) of total for {}: ".format(i + 1)))
        rebalanced_amount = percentage * total_amount
        print("Rebalanced amount: {:0.2f}".format(rebalanced_amount))
        rebalanced_amounts.append(rebalanced_amount)

    for i, new_amount in enumerate(rebalanced_amounts):
        old_amount = dict(enumerate(fund_amounts)).get(i, 0)
        print("Fund {} went from {:0.2f} to {:0.2f} (difference of {:0.2f})".format(i + 1, old_amount, new_amount, new_amount - old_amount))


if __name__ == "__main__":
    run()
