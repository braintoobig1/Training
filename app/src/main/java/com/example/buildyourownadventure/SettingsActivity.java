package com.example.buildyourownadventure;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.util.Log;

public class SettingsActivity extends AppCompatActivity {

    final String TAG = "demo"; //for tag

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_settings);

        Log.d(TAG, "onCreate: Settings"); //log successful launch
        setTitle("Settings");
    }
}