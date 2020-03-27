from parse import load_dataframes
import pandas as pd
import shutil


def sort_stores_by_score(dataframes, n=20, min_reviews=30):
    """
    Req. 1-2-1 각 음식점의 평균 평점을 계산하여 높은 평점의 음식점 순으로 `n`개의 음식점을 정렬하여 리턴합니다
    Req. 1-2-2 리뷰 개수가 `min_reviews` 미만인 음식점은 제외합니다.
    """

    # JOIN
    stores_reviews = pd.merge(
        dataframes["stores"], dataframes["reviews"], left_on="id", right_on="store"
    )
    scores_group = stores_reviews.groupby(["store", "store_name"])
    # print('#### group by 후 상태')
    # print(scores_group.head())
    
    # tt = scores_group['id_y'].count()
    # tt = tt[tt>min_reviews].reset_index()
    # print('#### count')
    # print(tt)

    scores = scores_group.mean().sort_values(by=["score"], ascending=False)
    # .sort_values(by=["score"], ascending=False) : 평균 평점 순
    
    # print('### score')
    # print(scores.head())

    # reset_index : 기존의 행 인덱스를 제거하고 인덱스를 데이터 열로 추가
    return scores.head(n=n).reset_index()


def get_most_reviewed_stores(dataframes, n=20):
    """
    Req. 1-2-3 가장 많은 리뷰를 받은 `n`개의 음식점을 정렬하여 리턴합니다
    """

    # dataframe에서 review테이블 추출
    stores_reviews = pd.merge(
        dataframes["stores"], dataframes["reviews"], left_on="id", right_on="store"
    )

    scores_group = stores_reviews.groupby(["store", "store_name"]) \
                                ["store"].count().reset_index(name='cnt') \
                                .sort_values(by=["cnt"], ascending=False)
    
    # 1. store, store_name으로 groupby
    # 2. store을 기준으로 count(), as cnt
    # 3. cnt기준으로 내림차순
    return scores_group.head(n=n).reset_index()


def get_most_active_users(dataframes, n=20):
    """
    Req. 1-2-4 가장 많은 리뷰를 작성한 `n`명의 유저를 정렬하여 리턴합니다.
    """

    users_reviews = pd.merge(
        dataframes["users"], dataframes["reviews"], left_on="id", right_on="user"
    )

    users_group = users_reviews.groupby(["user"]) \
                            ["user"].count().reset_index(name='cnt')\
                            .sort_values(by=["cnt"], ascending=False)
    
    return users_group.head(n=n).reset_index()


def main():
    data = load_dataframes()

    term_w = shutil.get_terminal_size()[0] - 1
    separater = "-" * term_w

    stores_most_scored = sort_stores_by_score(data)

    print("[최고 평점 음식점]")
    print(f"{separater}\n")
    for i, store in stores_most_scored.iterrows():
        print(
            "{rank}위: {store}({score}점)".format(
                rank=i + 1, store=store.store_name, score=store.score
            )
        )
    print(f"\n{separater}\n\n")

    stores_most_reviewed = get_most_reviewed_stores(data)

    print("[리뷰가 많은 음식점]")
    print(f"{separater}\n")
    for i, store in stores_most_reviewed.iterrows():
        print(
            "{rank}위: {store}({count}개)".format(
                rank=i + 1, store=store.store_name, count=store.cnt
            )
        )
    print(f"\n{separater}\n\n")

    users_most_reviewed = get_most_active_users(data)

    print("[리뷰 많이 작성한 유저]")
    print(f"{separater}\n")
    for i, user in users_most_reviewed.iterrows():
        print(
            "{rank}위: {user}({count}개)".format(
                rank=i + 1, user=user.user, count=user.cnt
            )
        )
    print(f"\n{separater}\n\n")


if __name__ == "__main__":
    main()
