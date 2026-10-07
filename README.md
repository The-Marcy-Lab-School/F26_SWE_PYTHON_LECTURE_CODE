# F26_SWE_PYTHON_LECTURE_CODE

1. Fork this repo 
2. Clone YOUR fork into your `development` folder

``` git clone git@github.com:YOUR_USERNAME/F26_SWE_PYTHON_LECTURE_CODE.git ```

3. `cd` into the repo and add THIS repo as the "upstream" source (this allows you to fetch changes from a parent repo)

``` git remote add upstream git@github.com:The-Marcy-Lab-School/F26_SWE_PYTHON_LECTURE_CODE.git ```

## When there are new lectures or lecture notes to fetch down

4. Fetch those changes/new lectures 

```git fetch upstream```

5.  Merge the changes/new lectures into YOUR fork 

```git merge upstream/main -m "meaningful message"```

6.  Push and changes you make to lectures/notes back to YOUR fork (these will be your personal notes/changes)

```git push origin main```
