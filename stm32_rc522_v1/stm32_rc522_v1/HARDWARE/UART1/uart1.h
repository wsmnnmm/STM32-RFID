#ifndef __USART_H
#define __USART_H
#include "stdio.h"	
#include "sys.h" 

struct Uart1_Recv{
   u8 len;//���ڽ��ճ���,������Ϊ255
	 u8 delay; //���ڳ�ʱ��ʱ������1��ʾ���ڽ��գ�1��ʾ������ɣ�0��ʾ�ȴ��µĽ���
	 u8 buf[255]; //���ڽ�������
};

extern struct Uart1_Recv uart1_recv;
	
//����봮���жϽ��գ��벻Ҫע�����º궨��
void Uart1_Init(u32 bound);
void Uart1_Rx_Clean();
#endif


