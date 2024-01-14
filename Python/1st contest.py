def contest_ratings(n, a, b):
    users_with_submissions = n - a  
    users_with_rating_below_1000 = b
    users_with_rating_above_1000 = users_with_submissions - users_with_rating_below_1000
    return users_with_submissions, users_with_rating_above_1000
n, a, b = map(int, input().split())
result = contest_ratings(n, a, b)
print(result[0], result[1])
