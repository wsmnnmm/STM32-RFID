#include "stm32f10x.h"
#include "delay.h"
#include "uart1.h"
#include "cardid.h"
int main(void)
{ 
	  char CARID[13]={0};//卡号
	  delay_ms(2000);
  	Uart1_Init(115200);//串口初始化
    CardId_Init();//RC522初始化
    while(1)
    {
			//获取刷卡信息
      if(CardId_Raed(CARID)==1){
				 //串口输出卡号
				printf("%s",CARID);
				WaitCardOff();
			 }
			//延时
		  delay_ms(1000);
    }
}

