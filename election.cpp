#include<stdio.h>
#include<string.h>
int main()
{
	char can[4][8] = { "can1","can2","can3","can4" }, ti[8], max = 0;//四位竞选人can1can2can3can4 


	int i, j, cannum[4] = { 0 };
	for (i = 0; i < 10; i++)
	{
		gets(ti);
		
		for (j = 0; j < 4; j++)
		{
			if (strcmp(can[j], ti) == 0)
				cannum[j]++;
		}
	}
	
	for (i = 1; i < 4; i++)
	{
		if (cannum[i] > cannum[i - 1])
			max = i;
	}
	printf("%s",can[max]);
} 
