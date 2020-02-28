from scipy import stats

class Z_score():
    @staticmethod
    def z_score(data):
        return stats.zscore(data)
