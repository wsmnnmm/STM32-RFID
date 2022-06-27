#include "stm32f10x.h"
#include "delay.h"
#include "uart1.h"
#include "cardid.h"
int main(void)
{ 
	  char CARID[13]={0};//����
	  delay_ms(2000);
  	Uart1_Init(115200);//���ڳ�ʼ��
    CardId_Init();//RC522��ʼ��
    while(1)
    {
			//��ȡˢ����Ϣ
      if(CardId_Raed(CARID)==1){
				 //�����������
				printf("%s",CARID);
				WaitCardOff();
			 }
			//��ʱ
		  delay_ms(1000);
    }
}

