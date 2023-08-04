#include <stdio.h>
int main(void) 
{
    int n;
    scanf("%d",&n);
    for(int i=0;i<n;i++)
    {
        int a,b,c;
        scanf("%d %d %d",&a,&b,&c);
        if(a*b%c==0)
        {
            printf("%d %d\n",a*b,c);
        }
        else if(b*c%a==0)
        {
            printf("%d %d\n",b*c,a);
        }
        else if(a*c%b==0)
        {
            printf("%d %d\n",a*c,b);
        }
        else
        {
            printf("-1\n");
        }
    }
 return 0;
}