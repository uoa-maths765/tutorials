    rng(1);  % fixed seed so the figure/report are reproducible

    %% ---- 1. Fixed / assumed parameters -------------------------------
    rho   = 1.2;     
    C     = 1;       % theoretical constant, assumed known
    E_true = 100;  

    %% ---- 2. Synthetic "photographic" data set ------------------------
    n_frames = 12;                          % a dozen times
    t = linspace(0.1, 1, n_frames);   % seconds, evenly spaced frames

    R_true = C * (E_true .* t.^2 ./ rho).^(1/5);

    noise_level = 0.03;                     % 3% multiplicative noise
    R_noisy = R_true + noise_level*randn(size(R_true));

    %% ---- 3. Fit: log R = slope * log t + intercept --------------------
    % Pretend we do NOT know E from here on.
    x = log(t(:));
    y = log(R_noisy(:));

    p = polyfit(x, y, 1);   % p(1) = slope, p(2) = intercept
    slope     = p(1)
    intercept = p(2);

    %% ---- 4. Recover E from the intercept -------------------------------
    % log R = (1/5) log(E/rho) + (2/5) log t   [since C = 1]
    % => intercept = (1/5) log(E/rho)
    % => E/rho = exp(5 * intercept)
    E_recovered = rho * exp(5 * intercept)

    %% ---- 5. Plot: data + fitted line on log-log axes -------------------

    plot(x,y, 'o');
    hold on;

    t_fit = log(linspace(min(t), max(t)));
    plot(t_fit, intercept+slope*t_fit);

    xlabel('log t (s)');
    ylabel('log R (m)');
    title('Taylor blast-wave: log R vs log t');
    grid on;
    box on;
    hold off;
