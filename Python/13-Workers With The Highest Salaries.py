# Question
  You have been asked to find the job titles of the highest-paid employees.
Your output should include the highest-paid title or multiple titles with the same salary.

# Link
  https://platform.stratascratch.com/coding/10353-workers-with-the-highest-salaries?code_type=2

# Answer
df = pd.merge(worker,title,left_on='worker_id',right_on='worker_ref_id')[['salary','worker_title']].sort_values('salary',ascending=False)
df.nlargest(2,'salary')['worker_title']


# Answer.2
title_worker_id = title.rename(columns={"worker_ref_id": "worker_id"})
merged_df = pd.merge(worker, title_worker_id, on="worker_id")
max_salary = merged_df[merged_df["salary"] == merged_df["salary"].max()][["worker_title"]].rename(columns={"worker_title": "best_paid_title"})

# Answer.3
title[title.worker_ref_id.isin(worker[worker.salary == worker.salary.max()].worker_id)]
