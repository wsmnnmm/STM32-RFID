#ifndef __USART_H
#define __USART_H
#include "stdio.h"	
#include "sys.h" 

struct Uart1_Recv{
   u8 len;//串口接收长度,最大接收为255
	 u8 delay; //串口超时延时，大于1表示正在接收，1表示接收完成，0表示等待新的接收
	 u8 buf[255]; //串口接收数据
};

extern struct Uart1_Recv uart1_recv;
	
//如果想串口中断接收，请不要注释以下宏定义
void Uart1_Init(u32 bound);
void Uart1_Rx_Clean();
#endif


