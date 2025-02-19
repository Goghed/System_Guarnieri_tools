document.addEventListener('DOMContentLoaded', function() {
    const sidebar = document.getElementById('sidebar');
    const menuIcon = document.getElementById('menu-icon');

    // Alternar menu lateral
    menuIcon.addEventListener('click', function() {
        sidebar.classList.toggle('collapsed');
    });

    // Gráficos com Chart.js
    const ctx1 = document.getElementById('myChart1').getContext('2d');
    const ctx2 = document.getElementById('myChart2').getContext('2d');
    const ctx3 = document.getElementById('myChart3').getContext('2d');

    // Gráfico de linha
    new Chart(ctx1, {
        type: 'line',
        data: {
            labels: ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun'],
            datasets: [{
                label: 'Ordens de Serviço',
                data: [12, 3, 5, 2, 3],
                borderColor: '#ffd700',
                tension: 0.4,
                fill: false,
                pointBackgroundColor: '#ffd700',
                pointBorderColor: '#fff',
                pointBorderWidth: 2,
                pointRadius: 5,
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            animations: {
                tension: {
                    duration: 1000,
                    easing: 'linear',
                    from: 1,
                    to: 0,
                    loop: true
                }
            },
            plugins: {
                datalabels: {
                    color: '#ffd700',
                    font: {
                        weight: 'bold',
                        size: 12
                    },
                    formatter: function(value) {
                        return value;
                    },
                    anchor: 'end',
                    align: 'top',
                }
            },
            scales: {
                y: {
                    beginAtZero: true,
                }
            }
        }
    });

    // Gráfico de barras
    new Chart(ctx2, {
        type: 'bar',
        data: {
            labels: ['Projetos', 'Manutenção', 'Varejo'],
            datasets: [{
                label: 'Abertas',
                data: [30, 20, 15],
                backgroundColor: [
                    'rgb(255, 99, 132)',
                    'rgb(255, 159, 64)',
                    'rgb(255, 205, 86)',                    
                ],
                borderColor: [
                    'rgb(255, 99, 132)',
                    'rgb(255, 159, 64)',
                    'rgb(255, 205, 86)',                    
                ],
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            animation: {
                duration: 4000,
                easing: 'easeInOutQuart',
            }
        }
    });

    // Gráfico de pizza
    new Chart(ctx3, {
        type: 'pie',
        data: {
            labels: ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun'],
            datasets: [{
                label: 'Ordens de Serviço',
                data: [12, 19, 3, 5, 2, 3],
                backgroundColor: ['#ffd700', '#ff6347', '#32cd32', '#1e90ff', '#8a2be2', '#ff1493'],
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            animation: {
                duration: 4000,
                easing: 'easeInOutQuart',
            },
            plugins: {
                tooltip: {
                    enabled: true
                },
                datalabels: {
                    formatter: (value, context) => {
                        const datapoints = context.chart.data.datasets[0].data;
                        function totalSum(total, datapoint) {
                            return total + datapoint;
                        }
                        const totalValue = datapoints.reduce(totalSum, 0);
                        const percentageValue = (value / totalValue * 100).toFixed(1);
                        return ` ${value} :  ${percentageValue}%`;
                    },
                    color: '#fff',
                    font: {
                        weight: 'bold',
                        size: 16
                    },
                    anchor: 'center',
                    align: 'center',
                }            
            }
        },
        plugins: [ChartDataLabels],
    });

    // Redimensionar gráficos ao redimensionar a janela
    window.addEventListener('resize', function() {
        if (myChart1) myChart1.resize();
        if (myChart2) myChart2.resize();
        if (myChart3) myChart3.resize();
    });
});