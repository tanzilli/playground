#ifndef  _GLOBAL_SENSOR_H_
#define  _GLOBAL_SENSOR_H_

struct _datasensincomp 
{
	float gyro_X[3]; //deg/sec
	float gyro_Y[3];
	float gyro_Z[3];
	float acc_X[3];  //g
	float acc_Y[3];
	float acc_Z[3];
	float mag_X[3];
	float mag_Y[3];
	float mag_Z[3];

} ;
typedef _datasensincomp datasensincomp;


struct _eulero_angle 
{
	float roll;
	float pitch;
	float yaw;
} ;
typedef _eulero_angle  eulero_angle ;


#endif
