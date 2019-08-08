package com.example.helloworld;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;

import java.io.IOException;
import java.util.Timer;
import java.util.TimerTask;

public class MainActivityLifeCycle extends AppCompatActivity {
    private Button Start_NormalActivity;
    private Button Start_DialogActivity;
    private String TAG="MainActivityLifeCycle";



    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        Log.d(TAG,"onCreate");
        setContentView(R.layout.activity_main_life_cycle);


        Start_NormalActivity=findViewById(R.id.Start_NormalActivity);
        Start_DialogActivity=findViewById(R.id.Start_DialogActivity);
        Start_NormalActivity.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = new Intent(MainActivityLifeCycle.this,NormalActivity.class);
                startActivity(intent);
            }
        });
        Start_DialogActivity.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                //建立一个Intent,startActivity 调用完成界面跳转
                Intent intent = new Intent(MainActivityLifeCycle.this,DialogActivity.class);
                startActivity(intent);
            }
        });
    }

    @Override
    protected void onStart() {
        super.onStart();
        Log.d(TAG,"OnStart");
        timer.schedule(task,10000);
    }

    @Override
    protected void onStop() {
        super.onStop();
        Log.d(TAG,"OnStop");
    }

    @Override
    protected void onDestroy() {
        super.onDestroy();
        Log.d(TAG,"OnDestroy");
    }

    @Override
    protected void onPause() {
        super.onPause();
        Log.d(TAG,"onPause");
    }

    @Override
    protected void onResume() {
        super.onResume();
        Log.d(TAG,"onResume");
    }

    @Override
    protected void onRestart() {
        super.onRestart();
        Log.d(TAG,"onRestart");
    }

    Timer timer = new Timer();
    TimerTask task = new TimerTask() {
        @Override
        public void run() {
            Intent intent = new Intent(MainActivityLifeCycle.this, NormalActivity.class);
            startActivity(intent);
            finish();
        }
    };

}
