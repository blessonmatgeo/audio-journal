// Fetch journal entries from the backend
async function fetchJournalEntries() {
    const response = await fetch('/api/journal');
    const data = await response.json();
    return data;
}

// Fetch analytics from the backend
async function fetchAnalytics() {
    const response = await fetch('/api/analytics');
    const data = await response.json();
    return data;
}

// Function to display journal entries in the table
function displayEntries(entries) {
    const journalEntriesContainer = document.getElementById('journal-entries');
    journalEntriesContainer.innerHTML = ''; // Clear previous entries

    entries.forEach(entry => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${entry.date}</td>
            <td>${entry.entry}</td>
            <td>${entry.mood} ${entry.emoji}</td>
            <td>${entry.sentiment}</td>
        `;
        journalEntriesContainer.appendChild(row);
    });
}

// Function to update sentiment analytics
function updateAnalytics(analytics) {
    document.getElementById('avg-sentiment').innerText = analytics.avg_sentiment.toFixed(2);
    document.getElementById('positive-count').innerText = analytics.positive_count;
    document.getElementById('negative-count').innerText = analytics.negative_count;
    document.getElementById('neutral-count').innerText = analytics.neutral_count;
}

// Initialize dashboard
async function initDashboard() {
    const entries = await fetchJournalEntries();
    const analytics = await fetchAnalytics();

    displayEntries(entries);
    updateAnalytics(analytics);
}

// Run on page load
window.onload = initDashboard;
