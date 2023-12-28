import collections
phishingemail = [
    "jackpotwin@lottery.com",
    "claimtheprize@mymoney.com",
    "youarethewinner@lottery.com",
    "luckywinner@mymoney.com",
    "spinthewheel@flipkart.com",
    "dealwinner@snapdeal.com",
    "luckywinner@snapdeal.com",
    "luckyjackpot@americanlottery.com",
    "claimtheprize@lootolottery.com",
    "youarelucky@mymoney.com"
]

email_domains = [email.split('@')[-1] for email in phishingemail]
domain_counts = collections.Counter(email_domains)
most_common_domain = domain_counts.most_common(1)[0][0]

print("Most Common Occurring domain is:", most_common_domain)
