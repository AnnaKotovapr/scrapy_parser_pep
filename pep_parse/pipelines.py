import csv
import datetime as dt
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

FIELDS_NAME = ('Статус', 'Количество')
RESULTS_DIR = 'results'
TIME_FORMAT = '%Y-%m-%d_%H-%M-%S'
TIMENOW = dt.datetime.now().strftime(TIME_FORMAT)
FILENAME = 'status_summary_{time}.csv'


class PepParsePipeline:

    def open_spider(self, spider):

        self.results = {}
        self.result_dir = BASE_DIR / RESULTS_DIR
        self.result_dir.mkdir(exist_ok=True)

    def process_item(self, item, spider):

        pep_status = item['status']
        self.results[pep_status] = self.results.get(pep_status, 0) + 1
        return item

    def close_spider(self, spider):
        file_dir = self.result_dir / FILENAME.format(
            time=TIMENOW)
        with open(file_dir, mode='w', encoding='utf-8') as f:
            writer = csv.writer(f, dialect='unix')
            writer.writerow(FIELDS_NAME)

            #  как я понимаю, чтобы результат выводился в табличном виде,
            #  нужно делать через for
            data_to_write = [
                [status, count] for status, count in self.results.items()]
            data_to_write.append(
                ['Total', sum(self.results.values())]
            )
            writer.writerows(data_to_write)
