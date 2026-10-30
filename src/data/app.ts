// Single source of truth for the app legal and support pages.
// Every page under src/pages/apps/[slug]/ reads from here.

// The app name. The URL slug follows automatically.
export const name = "Strandmark";

export const slug = name.toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "");

// Placeholder address. Replace it with the real support address before publishing.
export const supportEmail = "support@rishavkatoch.me";

export const lastUpdated = "31 October 2026";

export const developer = "Rishav Katoch";

// Set to the App Store URL once the app is live. While null, the badge is hidden.
export const appStoreUrl: string | null = null;

export const eulaUrl = "https://www.apple.com/legal/internet-services/itunes/dev/stdeula/";
