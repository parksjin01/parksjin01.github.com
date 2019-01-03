---
title: "Seventh.cc 예제 파일 설명"
date: "2019-01-03"
category: "ns3"
---

### Seventh example scenario

일곱번째 파일역시 다섯번째 파일과 똑같은 네트워크 코드를 사용하고 있습니다. 이미 다섯번째, 여섯번째 예제 파일에서 네트워크에 대한 설명을 했기 때문에 네트워크 설명은 넘어가도록 하겠습니다. 여섯번째 예제 파일은 다섯번째 예제 파일에 추가적으로 Tracing 데이터를 파일로 저장하는 방법에 대해 알아보았습니다. 일곱번째 예제 파일은 여섯번째 예제 파일에 추가적으로 Gnuplot 프로그램을 이용하여 그래프를 그리는 방법에 대해 알아보도록 하겠습니다. Gnuplot은 그래프를 그리는데 사용하는 프로그램입니다. 지난번 예제파일에서는 그래프를 그리기 위하여 Tracing 데이터가 저장된 파일을 파이썬 코드를 이용하여 그래프로 시각화 하였지만 그럴 필요없이 ns-3에 포함되어있는 GnuplotHelper를 이용하여 그래프로 시각화할 수 있습니다. 이번 포스팅에서는 GnuplotHelper를 이용하여 시각화하는 방법을 살펴보도록 하겠습니다.

```c++
// Use GnuplotHelper to plot the packet byte count over time
GnuplotHelper plotHelper;

// Configure the plot.  The first argument is the file name prefix
// for the output files generated.  The second, third, and fourth
// arguments are, respectively, the plot title, x-axis, and y-axis labels
plotHelper.ConfigurePlot ("seventh-packet-byte-count",
                          "Packet Byte Count vs. Time",
                          "Time (Seconds)",
                          "Packet Byte Count");

// Specify the probe type, trace source path (in configuration namespace), and
// probe output trace source ("OutputBytes") to plot.  The fourth argument
// specifies the name of the data series label on the plot.  The last
// argument formats the plot by specifying where the key should be placed.
plotHelper.PlotProbe (probeType,
                      tracePath,
                      "OutputBytes",
                      "Packet Byte Count",
                      GnuplotAggregator::KEY_BELOW);

// Use FileHelper to write out the packet byte count over time
FileHelper fileHelper;

// Configure the file to be written, and the formatting of output data.
fileHelper.ConfigureFile ("seventh-packet-byte-count",
                          FileAggregator::FORMATTED);

// Set the labels for this formatted output file.
fileHelper.Set2dFormat ("Time (Seconds) = %.3e\tPacket Byte Count = %.0f");

// Specify the probe type, trace source path (in configuration namespace), and
// probe output trace source ("OutputBytes") to write.
fileHelper.WriteProbe (probeType,
                       tracePath,
                       "OutputBytes");

```

### 실행결과

```shell
seventh-packet-byte-count-0.txt  seventh-packet-byte-count-1.txt    seventh-packet-byte-count.dat    seventh-packet-byte-count.plt     seventh-packet-byte-count.sh
```

이번에도 여섯번째 예제 파일처럼 추가된 부분만 소개하도록 하겠습니다. 이번에는 워낙 영어 주석이 잘 달려 있어서 따로 주석을 추가하지 않았습니다. `Seventh.cc` 시나리오를 실행하게 되면 위와 같은 파일들이 생성되는 것을 알 수 있습니다. 이 파일들이 Gnuplot을 이용하여 그래프를 그리는데 사용하는 파일입니다. 생성된 파일들 중 `seventh-packet-byte-count.sh`에게 `chmod 0777 seventh-packet-byte-count.sh` 명령어를 이용하여 실행권한을 준뒤 실행을 시키면 아래와 같은 그래프가 그려지게 됩니다.

![seventh-packet-byte-count](https://i.imgur.com/CxS0We0.png)

위 그래프는 조금 엉성하지만 좀더 그래프를 그리기 위한 코드를 작성하면 깔끔한 그래프를 그릴수도 있습니다. 아니면 이전 여섯 번째 예제 프로그램에서 소개해드린 대로 Tracing 데이터 파일을 이용하여 사용하기 편한 그래프 시각화 툴, 라이브러리 등을 이용하여 그리셔도 됩니다. 이번 포스팅으로 ns-3가 제공하는 예제 파일은 끝났네요. 다음 포스팅에서는 ns-3가 제공하지 않는 어플리케이션을 추가하는 포스팅을 준비하여 소개하도록 하겠습니다.
