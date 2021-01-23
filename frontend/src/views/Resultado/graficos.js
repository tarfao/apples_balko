export const bars = (dataAxis, data, title, subtext = null, colorBar = "#228B22") => {
    return {
        title: [
            {
                text: title,
                subtext: subtext,
            },
        ],
        xAxis: {
            data: dataAxis,
            axisLabel: {
                inside: true,
                textStyle: {
                    color: "#fff",
                },
            },
            axisTick: {
                show: false,
            },
            axisLine: {
                show: false,
            },
            z: 10,
        },
        yAxis: {
            axisLine: {
                show: false,
            },
            axisTick: {
                show: false,
            },
            axisLabel: {
                textStyle: {
                    color: "#999",
                },
            },
        },
        dataZoom: [
            {
                type: "inside",
            },
        ],
        series: [
            {
                // For shadow
                type: "bar",
                itemStyle: {
                    color: "rgba(0,0,0,0.05)",
                },
                barGap: "-100%",
                barCategoryGap: "40%",
                animation: false,
            },
            {
                type: "bar",
                data: data,
            },
        ],
        color: colorBar,
        resize: {
            width: 500
        }
    }
}